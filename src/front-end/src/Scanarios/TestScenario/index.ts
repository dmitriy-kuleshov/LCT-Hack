import { Scenario } from '../types'
import { GetDate, TestNodesNames } from './commands'
import {
  DateNode,
  Stage1Node,
  Stage2Node,
  Stage3Node,
  StartNode,
} from './nodes'

export const TestNodes: Scenario<TestNodesNames> = {
  [TestNodesNames.start]: StartNode,
  [TestNodesNames.testNode1]: Stage1Node,
  [TestNodesNames.testNode2]: Stage2Node,
  [TestNodesNames.testNode3]: Stage3Node,
  [TestNodesNames.getDate]: DateNode,
}
